<script>
	import { stores } from '@sapper/app';

	const { page } = stores();

	export let segment;
</script>

<style>
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

	[aria-current] {
		color: #202020;
		font-weight: 700;
		position: relative;
		/* text-decoration: underline; */
	}

	/* [aria-current]::after {
		background: linear-gradient(135deg, rgba(159, 200, 164, 1) 0%, rgba(140, 193, 182, 1) 100%);
		content: "";
		height: 4px;
		position: absolute;
			bottom: -2px;
			left: -0.5rem;
			right: -0.5rem;
		z-index: 1;
	} */

	/* ul {
		display: flex;
		justify-content: flex-end;
		list-style-type: none;
		width: 100%;
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
		line-height: 2rem;
		padding: 1.4rem 0 0.6rem;
		text-decoration: none;
	}

	a span {
		display: none;
	}

	[aria-current] {
		color: #202020;
		text-decoration: underline;
	} */
</style>

<nav>
	<ul>
		<li>
			<!-- <a aria-current='{segment === "overview" ? "page" : undefined}' href="overview"> -->
			<a aria-current={$page.path.includes("overview") ? "page" : undefined} href={$page.path.includes("documentation") ? "documentation/overview" : "overview"}>
				Overview
				<span>Products</span>
			</a>
		</li>
		<li>
			<!-- <a aria-current='{segment === "users" ? "page" : undefined}' href="users"> -->
			<a aria-current={$page.path.includes("users") ? "page" : undefined} href={$page.path.includes("documentation") ? "documentation/users/installation/gettingstarted" : "users"}>
				Users
				<span>Smart Home</span>
			</a>
		</li>
		<li>
			<!-- <a aria-current='{segment === "developers" ? "page" : undefined}' href="developers"> -->
			<a aria-current={$page.path.includes("developers") ? "page" : undefined} href={$page.path.includes("documentation") ? "documentation/developers" : "developers"}>
				Developers
				<span>Internet of Things</span>
			</a>
		</li>
		<li>
			<!-- <a aria-current='{segment === "businesses" ? "page" : undefined}' href="businesses"> -->
			<a aria-current={$page.path.includes("businesses") ? "page" : undefined} href={$page.path.includes("documentation") ? "documentation/businesses" : "businesses"}>
				Businesses
				<span>Consumer Products</span>
			</a>
		</li>
	</ul>
</nav>
