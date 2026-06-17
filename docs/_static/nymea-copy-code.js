// Normalize any "auto" theme immediately — before pydata's deferred script runs
(function () {
  var mode = localStorage.getItem("mode");
  if (!mode || mode === "auto") {
    mode = "dark";
    localStorage.setItem("mode", "dark");
    localStorage.setItem("theme", "dark");
  }
  document.documentElement.dataset.mode = mode;
  document.documentElement.dataset.theme = mode;
}());

(function () {
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }

    var textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.setAttribute("readonly", "");
    textarea.style.position = "fixed";
    textarea.style.left = "-9999px";
    document.body.appendChild(textarea);
    textarea.select();

    try {
      document.execCommand("copy");
      return Promise.resolve();
    } finally {
      document.body.removeChild(textarea);
    }
  }

  function initTabs() {
    var tabGroups = document.querySelectorAll(".nymea-tabs");

    tabGroups.forEach(function (group) {
      var tabs = Array.prototype.slice.call(group.querySelectorAll("[role='tab']"));
      var panels = Array.prototype.slice.call(group.querySelectorAll("[role='tabpanel']"));

      tabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
          tabs.forEach(function (item) {
            item.setAttribute("aria-selected", item === tab ? "true" : "false");
          });

          panels.forEach(function (panel) {
            panel.hidden = panel.id !== tab.getAttribute("aria-controls");
          });
        });
      });
    });
  }

  function addCopyButtons() {
    var blocks = document.querySelectorAll("div[class*='highlight-'], .nymea-code-block");

    blocks.forEach(function (block) {
      var pre = block.querySelector("pre");
      if (!pre || block.querySelector(".nymea-copy-code")) {
        return;
      }

      var button = document.createElement("button");
      button.className = "nymea-copy-code";
      button.type = "button";
      button.innerHTML = '<span class="nymea-copy-icon" aria-hidden="true"></span>';
      button.setAttribute("aria-label", "Copy code");
      button.setAttribute("title", "Copy code");

      button.addEventListener("click", function () {
        copyText(pre.innerText).then(function () {
          button.classList.add("nymea-copy-code-done");
          button.setAttribute("aria-label", "Copied");
          button.setAttribute("title", "Copied");
          window.setTimeout(function () {
            button.classList.remove("nymea-copy-code-done");
            button.setAttribute("aria-label", "Copy code");
            button.setAttribute("title", "Copy code");
          }, 1400);
        });
      });

      block.appendChild(button);
    });
  }

  function patchThemeToggle() {
    document.querySelectorAll(".theme-switch-button").forEach(function (btn) {
      var fresh = btn.cloneNode(true);
      btn.parentNode.replaceChild(fresh, btn);
      fresh.addEventListener("click", function () {
        var next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
        document.documentElement.dataset.mode = next;
        document.documentElement.dataset.theme = next;
        localStorage.setItem("mode", next);
        localStorage.setItem("theme", next);
        document.querySelectorAll(".dropdown-menu").forEach(function (el) {
          el.classList.toggle("dropdown-menu-dark", next === "dark");
        });
      });
    });
  }

  function init() {
    initTabs();
    addCopyButtons();
    window.setTimeout(patchThemeToggle, 0);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
