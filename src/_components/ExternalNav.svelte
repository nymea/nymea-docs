<script>
	import { isActive, url, layout, route, routes } from '@sveltech/routify';
</script>

<style>
	nav {
		display: none;
	}

	@media only screen and (min-width: 48em) {
		nav {
			display: block;
		}
	}

	ul {
		display: flex;
		height: var(--header-height);
		justify-content: flex-end;
		list-style-type: none;
    /* padding-right: 1.5rem;
		padding-left: 3rem; */
		padding: 0 1.5rem 0 0;
	}

	li {
		margin-left: 1.5rem;
	}

	li:first-child {
		margin-left: 0;
	}

	/* li:first-child {
    margin-left: 0;
    margin-right: auto;
	} */

	a {
		color: #676767;
		display: block;
		height: 4.5rem;
		padding: 1.5rem 0;
		text-decoration: none;
	}

  ion-icon {
		color: #202020;
    font-size: 1.5rem;
  }

  /* .twitter:hover {
    color: #1da1f2;
  }

  .github:hover {
    color: #231e1b;
  } */
</style>

<nav>
	<ul class="menu">
		<li>
			<a href="https://forum.nymea.io/" target="_blank" rel="noopener">
				<ion-icon src="/img/discourse-bw.svg" class="discourse"></ion-icon>
			</a>
		</li>
		<li>
			<a href="https://t.me/nymeacommunity" target="_blank" rel="noopener">
				<ion-icon src="/img/telegram-bw.svg" class="telegram"></ion-icon>
			</a>
		</li>
		<li>
			<a href="https://twitter.com/nymea_io" target="_blank" rel="noopener">
        <ion-icon name="logo-twitter" class="twitter"></ion-icon>
      </a>
		</li>
		<li>
			<a href="https://github.com/nymea" target="_blank" rel="noopener">
        <ion-icon name="logo-github" class="github"></ion-icon>
      </a>
		</li>
	</ul>
</nav>
