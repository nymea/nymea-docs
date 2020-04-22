<script>
	import { stores } from '@sapper/app';
	import Header from '../components/Header.svelte';
	import Nav from '../components/Nav.svelte';
	import Layout from '../components/Layout.svelte';
	// import SidebarLayout from '../components/SidebarLayout.svelte';
	import SubNav from '../components/SubNav.svelte';
	import ContentNav from '../components/ContentNav.svelte';
	import items from '../routes/_menu-manual.js';

	const { preloading, page, session } = stores();

	export let segment;

	console.log('page', page);

	$: currentItem = items.find((item) => {
		// console.log('item', item.id === segment, segment, item);
		return item.id === segment;
	});
	$: segmentItems = currentItem ? currentItem.children : [];
</script>

<style>
	.nav-page {
		/* background-color: #fafafa; */
		height: auto;
		width: 20rem;
	}

	.nav-content {
		/* background-color: #fafafa; */
		height: auto;
		width: 20rem;
	}

	.nav-content.active {
		border-left: 1px solid #efefef;
	}

	main {
		padding: 3rem;
	}

	.main-inner {
		max-width: 40em;
	}

	ul {
		list-style-type: none;
		margin: 0;
	}
	a {
		color: #222;
		display: block;
		text-decoration: none;
	}
	a span {
		display: none;
		font-size: 0.8em;
		text-transform: uppercase;
	}
</style>

<Layout>
	<div class="nav-page" slot="sidebar-page">
		{#if $page.path.includes('documentation')}
			<SubNav base="{segment}/documentation" {segment} items={segmentItems} />
		{/if}
	</div>

	<div slot="content">
		<Header>
			<Nav {segment} />
		</Header>

		<main>
			<div class="main-inner">
				<slot></slot>
			</div>
		</main>
	</div>

	<div class="nav-content {$page.path.includes('documentation') ? 'active' : ''}" slot="sidebar-content">
		{#if $page.path.includes('documentation')}
			<ContentNav />
		{/if}
	</div>
</Layout>