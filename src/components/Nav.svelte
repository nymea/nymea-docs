<script>
	export let segment;
</script>

<style>
	ul {
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
	}
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
				Users
				<span>Smart Home</span>
			</a>
		</li>
		<li>
			<a aria-current='{segment === "developers" ? "page" : undefined}' href="developers">
				Developers
				<span>Internet of Things</span>
			</a>
		</li>
		<li>
			<a aria-current='{segment === "businesses" ? "page" : undefined}' href="businesses">
				Businesses
				<span>Consumer Products</span>
			</a>
		</li>
	</ul>
</nav>
