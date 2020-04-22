<script>
	export let segment;
</script>

<style>
	ul {
		display: flex;
		justify-content: space-between;
		list-style-type: none;
		/* margin-left: -1.5rem; */
	}

	li {
		/* display: inline-block; */
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
	}

	/* nav {
		border-bottom: 1px solid rgba(255,62,0,0.1);
		font-weight: 300;
		padding: 0 1em;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	ul::after {
		content: '';
		display: block;
		clear: both;
	}

	li {
		display: block;
		float: left;
	}

	[aria-current] {
		position: relative;
		display: inline-block;
	}

	[aria-current]::after {
		position: absolute;
		content: '';
		width: calc(100% - 1em);
		height: 2px;
		background-color: rgb(255,62,0);
		display: block;
		bottom: -1px;
	}

	a {
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	} */
</style>

<nav>
	<ul>
		<li>
			<a aria-current='{segment === "overview" ? "page" : undefined}' href="overview">
				Overview
				<span>Products</span>
			</a>
		</li>
		<li>
			<a aria-current='{segment === "users" ? "page" : undefined}' href="users">
				For Users
				<span>Smart Home</span>
			</a>
		</li>
		<li>
			<a aria-current='{segment === "developers" ? "page" : undefined}' href="developers">
				For Developers
				<span>Internet of Things</span>
			</a>
		</li>
		<li>
			<a aria-current='{segment === "businesses" ? "page" : undefined}' href="businesses">
				For Businesses
				<span>Consumer Products</span>
			</a>
		</li>
	</ul>
</nav>
