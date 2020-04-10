<script>
  const path = window.location.pathname.split('/').pop();
  const title = path.replace('-', ' ').charAt(0).toUpperCase() + path.replace('-', ' ').slice(1);
</script>

<style></style>

<h1>{title}</h1>
<slot></slot>
