<script>
	import { isActive, url, layout, route, routes } from '@sveltech/routify';

	let hidden = true;

	function toggle() {
		console.log('toggle');
		hidden = !hidden;
	}
</script>

<style>
	nav {
		background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: saturate(50%) blur(4px);
    -webkit-backdrop-filter: saturate(50%) blur(4px);
		display: block;
		height: 100vh;
		position: fixed;
			bottom: 0;
			left: 0;
			right: 0;
			top: 0;
		z-index: 0;
	}

	nav.hidden {
		display: none;
	}

	.toggle {
		display: block;
		float: right;
		font-size: 1.5rem;
		margin: 1.5rem;
		position: fixed;
			right: 0;
			top: 0;
		z-index: 1;
	}

	@media only screen and (min-width: 48em) {
		nav,
		nav.hidden {
			display: block;
			position: initial;
		}


		nav {
			background-color: transparent;
			backdrop-filter: initial;
			-webkit-backdrop-filter: initial;
		}

		.toggle {
			display: none;
		}
	}
	
	ul {
		height: 100vh;
		padding: 3rem;
	}

	li {
		border-bottom: 1px solid var(--silver-darken-10);
	}

	@media only screen and (min-width: 48em) {
		nav {
			height: var(--header-height);
			position: static;
				bottom: initial;
				left: initial;
				right: initial;
				top: initial;
		}

		ul {
			display: flex;
			height: var(--header-height);
			/* justify-content: flex-end; */
			list-style-type: none;
			padding: 0;
			padding-right: 1.5rem;
		}

		li {
			border-bottom: 0;
			margin-left: 1.5rem;
		}

		li:first-child {
			margin-left: 0;
		}
	}

	a {
		color: #676767;
		display: block;
		padding: 1.5rem 0;
		text-decoration: none;
	}

	/* [aria-current], */
	.active {
		color: #202020;
		font-weight: 700;
		position: relative;
		/* text-decoration: underline; */
	}
</style>

{#if hidden === true}
	<ion-icon name="menu" class="toggle" on:click={() => toggle()}></ion-icon>
{:else}
	<ion-icon name="close" class="toggle" on:click={() => toggle()}></ion-icon>
{/if}

<nav class:hidden>
	<ul class="menu">
		<li>
			<a class:active={$isActive('/users')} href={$url('/users')}>Users</a>
		</li>
		<li>
			<a class:active={$isActive('/developers')} href={$url('/developers')}>Developers</a>
		</li>
		<li>
			<a class:active={$isActive('/businesses')} href={$url('/businesses')}>Businesses</a>
		</li>
		<li>
			<a class:active={$route.path.includes('/documentation')} href={$url('/documentation/overview/about-nymea')}>Documentation</a>
		</li>
	</ul>
	<!-- {#if $route.path.includes('/documentation')}
		<ul class="menu">
			<li class="main">
				<a class:active={$isActive('/documentation/overview')} href={$url('/documentation/overview')}>Documentation</a>
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
			<li class="main">
				<a class:active={$route.path === '/index'} href={$url('/')}>Home</a>
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
	{/if} -->
</nav>
