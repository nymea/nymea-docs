<script>
	import Wrapper from '../components/Wrapper.svelte';
	import Row from '../components/Row.svelte';
	import Col from '../components/Col.svelte';
</script>

<style>
	#introduction {
		--header-height: 7.5rem;
		display: flex;
		flex-direction: column;
		height: calc(100vh - var(--header-height));
		justify-content: center;
		margin: calc(-1 * var(--header-height)) 0 4.5rem;
		padding-top: 7.5rem;
	}

	#introduction h1 {
		color: #676767;
		font-size: 2.25rem;
		line-height: 3rem;
	}

	#introduction h2 {
		font-size: 4.5rem;
		font-weight: 500;
		line-height: 4.5rem;
		margin: 0  0 3rem;
	}

	#introduction ul {
		list-style-type: none;
	}

	#introduction li {
		font-size: 1.875rem;
		font-weight: 300;
		line-height: 3rem;
		text-decoration: none;
	}

	#introduction ion-icon {
		font-size: 1.5rem;
		margin: 0 0.75rem -0.2rem 0;
	}

	a.button {
		align-self: flex-start;
		appearance: none;
		background: rgba(159, 200, 164, 1);
		background: linear-gradient(135deg, rgba(159, 200, 164, 1) 0%, rgba(140, 193, 182, 1) 100%);
		border-radius: 6px;
		color: #fff;
		display: block;
		flex-basis: 1;
		margin: 3rem 0 0;
		padding: 0.75rem 1.5rem;
		text-decoration: none;
	}

	#introduction a.button ion-icon {
		font-size: 1rem;
		margin: 0 0 -0.1rem 0.75rem;
	}
</style>

<svelte:head>
	<title>nymea</title>
</svelte:head>

<Wrapper>
	<section id="introduction">
		<Row>
			<Col offset="20" width="60">
				<h1>nymea</h1>
				<h2>The Open IoT Stack</h2>
				<ul>
					<!-- <li><ion-icon name="checkmark-circle"></ion-icon>connect</li>
					<li><ion-icon name="checkmark-circle"></ion-icon>integrate</li>
					<li><ion-icon name="checkmark-circle"></ion-icon>stay independent</li> -->
					<li><ion-icon name="checkmark-circle"></ion-icon>Connect products & services</li>
					<li><ion-icon name="checkmark-circle"></ion-icon>Integrate with platforms</li>
					<li><ion-icon name="checkmark-circle"></ion-icon>Stay independent through "local first"</li>
				</ul>
				<a class="button" href="documentation/overview">Get started<ion-icon name="arrow-forward"></ion-icon></a>
			</Col>
		</Row>
	</section>
</Wrapper>

<Wrapper>
	<section id="what-1">
		<Row>
			<Col offset="20" width="60">
				<h2>From individual features to a full blown IoT device</h2>
				<p>Nymea is an open source IoT stack. It is used to build smart IoT devices, smart home gateways or enable individual IoT related features in connected products. We follow a "local first" approach, which means nymea will keep users data private and will still be functional even without Internet connection. Obviously, cloud integration is still available if wanted.</p>
			</Col>
		</Row>
	</section>
</Wrapper>

<Wrapper>
	<section id="for-whom">
		<Row>
			<Col offset="20" width="20">
				<h2>For Users</h2>
				<p>nymea gets you up and running with your smart home setup in no time. Just install nymea:core and nymea:app and you're all set with a powerful smart home solution that does not require powerful hardware or fiddling with cryptic configuration files. Using 100% free and open source software.</p>
			</Col>
			<Col width="20">
				<h2>For Developers</h2>
				<p>When you're building your own IoT device, nymea will help with all the software efforts. Whether it's connecting your device to others, adding easy set-up features, creating smart hubs for for all your devices or adding control and setup frontends, nymea's got your back.</p>
			</Col>
			<Col width="20">
				<h2>For Businesses</h2>
				<p>Building IoT enabled customer grade products can be hard. We've ramped up with all the required know-how and with the nymea stack we'll be supporting your business. Whether it's fast prototyping and consulting, providing needed components, building entire products or caring for deployments and updates. Together with our partners we offer in-field experience for all of those aspects.</p>
			</Col>
		</Row>
	</section>
</Wrapper>

<Wrapper>
	<section id="how">
		<Row>
			<Col offset="20" width="60">
				<h2>Nymea Software Stack</h2>
				<p>Simple, yet powerful.</p>
				<p>The nymea core stack is written in C++ and Qt. This results in low hardware requirements and high performance. To ease and speed up development time, individual integrations and automation behaviours can be added with JavaScript.</p>
			</Col>
		</Row>
	</section>
</Wrapper>

<Wrapper>
	<section id="what-2">
		<Row>
			<Col offset="20" width="60">
				<h2>Built for connected devices</h2>
				<p>Connect lighting, media, heatings, irrigations and sprinklers, garage doors, alarm systems and many more to a centralized, local and privacy focused control center with nymea. Or build your device running nymea to connect and integrate with other solutions, such as Alexa or Google Home.</p>
			</Col>
		</Row>
	</section>
</Wrapper>

<Wrapper>
	<section id="why">
		<Row>
			<Col offset="20" width="60">
				<h2>Affair of the heart</h2>
				<p>We think that IoT devices, especially inside your home do not have to be cloud connected all the time. Privacy and reliability are our main concerns. With that in mind we build anything we do with a offline-first approach. This results in blazing fast reaction times, full control over personal data and guarantees your product won't be rendered useless if the cloud provider you've been betting on shuts down their service.
The nymea Team</p>
			</Col>
		</Row>
	</section>
</Wrapper>

<Wrapper>
	<section id="showcases">
		<Row>
			<Col offset="20" width="60">
				<h2>Showcase</h2>
			</Col>
		</Row>
	</section>
</Wrapper>