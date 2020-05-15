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
		height: 6rem;
		justify-content: flex-end;
		list-style-type: none;
	}

	li {
		margin-left: 1.5rem;
	}

	li:first-child {
		margin-left: 0;
	}

	a {
		color: #676767;
		display: block;
		padding: 2.25rem 0;
		text-decoration: none;
	}

	a span {
		display: none;
	}

	/* [aria-current], */
	.active {
		color: #202020;
		font-weight: 700;
		position: relative;
		/* text-decoration: underline; */
	}
</style>

<nav>
	{#if $route.path.includes('/documentation')}
		<ul class="menu">
			<li>
				<a class:active={$isActive('/documentation/overview')} href={$url('/documentation/overview')}>Overview</a>
			</li>
			<li>
				<a class:active={$isActive('/documentation/users')} href={$url('/documentation/users/installation/gettingstarted')}>Users</a>
			</li>
			<li>
				<a class:active={$isActive('/documentation/developers')} href={$url('/documentation/developers')}>Developers</a>
			</li>
			<li>
				<a class:active={$isActive('/documentation/businesses')} href={$url('/documentation/businesses')}>Businesses</a>
			</li>
		</ul>
	{:else}
		<ul class="menu">
			<li>
				<a class:active={$route.path === '/index'} href={$url('/')}>Overview</a>
			</li>
			<li>
				<a class:active={$isActive('/users')} href={$url('/users')}>Users</a>
			</li>
			<li>
				<a class:active={$isActive('/developers')} href={$url('/developers')}>Developers</a>
			</li>
			<li>
				<a class:active={$isActive('/businesses')} href={$url('/businesses')}>Businesses</a>
			</li>
		</ul>
	{/if}
</nav>
