<script>
	import { stores } from '@sapper/app';
	import Wrapper from '../../components/Wrapper.svelte';
	import Row from '../../components/Row.svelte';
	import Col from '../../components/Col.svelte';

	import Header from '../../components/Header.svelte';
	import Nav from '../../components/Nav.svelte';
	
	import Layout from '../../components/Layout.svelte';
	// import SidebarLayout from '../components/SidebarLayout.svelte';
	import SubNav from '../../components/SubNav.svelte';
	import ContentNav from '../../components/ContentNav.svelte';
	import items from '../../routes/_menu-manual.js';

	const { preloading, page, session } = stores();

	export let segment;

	let styles = {
		// '--background-color': '#fff',
		// '--background-color-left': '#fafafa',
		// '--background-color-right': '#fff'
	};

	console.log('page', page);

	// $: segment = $page.path.substring($page.path.lastIndexOf('documentation/') + 1).split('/')[0];
	$: currentItem = items.find((item) => {
		// console.log('item', item.id === segment, segment, item);
		return item.id === segment;
	});
	$: segmentItems = currentItem ? currentItem.children : [];
</script>

<style>
	/* .nav-page,
	.nav-content,
	.content {
		padding-top: 7.5rem;
	} */

	/* .nav-page {
		background-color: #fafafa;
		height: auto;
		width: 20rem;
	}

	.nav-content { */
		/* background-color: #fafafa; */
		/* height: auto;
		width: 20rem;
	}

	.nav-content.active {
		border-left: 1px solid #efefef;
	} */

	main {
		--header-height: 7.5rem;
		border-left: 1px solid #efefef;
		border-right: 1px solid #efefef;
		height: calc(100vh - var(--header-height));
		overflow: scroll;
		padding: 3rem;
	}

	/* .main-inner {
		max-width: 40em;
	} */

	/* ul {
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
	} */
</style>

<Wrapper {styles}>
	<Row>
		<Col width="20">
			{#if $page.path.includes('documentation')}
				<SubNav base="documentation/{segment}" {segment} items={segmentItems} />
			{/if}
		</Col>
		<Col width="60">
			<main>
				<slot></slot>
			</main>
		</Col>
		<Col width="20">
			{#if $page.path.includes('documentation')}
				<!-- <ContentNav></ContentNav> -->
			{/if}
		</Col>
	</Row>
	<!-- <Row>
		<Col width="20">
			{#if $page.path.includes('documentation')}
				<SubNav base="documentation/{segment}" {segment} items={segmentItems} />
			{/if}
		</Col>
		<Col width="65">
			<main>
				<slot></slot>
			</main>
		</Col>
		<Col width="15">
			{#if $page.path.includes('documentation')}
				<ContentNav />
			{/if}
		</Col>
	</Row> -->
</Wrapper>

<!-- <Wrapper {styles}>
	<Layout>
		<div class="nav-page" slot="sidebar-page"> -->
			<!-- <p>{$page.path}</p>
			<p>{segment}</p>
			<p>{$page.path.substring($page.path.lastIndexOf('/') + 1)}</p> -->
			<!-- {#if $page.path.includes('documentation')}
				<SubNav base="{segment}/documentation" {segment} items={segmentItems} /> -->
				<!-- <SubNav base="documentation/{segment}" {segment} items={segmentItems} /> -->
			<!-- {/if}
		</div> -->

		<!-- <div slot="content"> -->
			<!-- <Header>
				<Nav {segment} />
			</Header> -->

			<!-- <main>
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
</Wrapper> -->