/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');

const CompLibrary = require('../../core/CompLibrary.js');

const MarkdownBlock = CompLibrary.MarkdownBlock; /* Used to read markdown */
const Container = CompLibrary.Container;
const GridBlock = CompLibrary.GridBlock;

class HomeSplash extends React.Component {
  render() {
    const {siteConfig, language = ''} = this.props;
    const {baseUrl, docsUrl} = siteConfig;
    const docsPart = `${docsUrl ? `${docsUrl}/` : ''}`;
    const langPart = `${language ? `${language}/` : ''}`;
    const docUrl = doc => `${baseUrl}${docsPart}${langPart}${doc}`;

    const SplashContainer = props => (
      <div className="homeContainer">
        <div className="homeSplashFade">
          <div className="wrapper homeWrapper">{props.children}</div>
        </div>
      </div>
    );

    const Logo = props => (
      <div className="projectLogo">
        <img src={props.img_src} alt="Project Logo" />
      </div>
    );

    const ProjectTitle = () => (
      <h2 className="projectTitle">
        {siteConfig.title}
        <small>{siteConfig.tagline}</small>
      </h2>
    );

    const PromoSection = props => (
      <div className="section promoSection">
        <div className="promoRow">
          <div className="pluginRowBlock">{props.children}</div>
        </div>
      </div>
    );

    const Button = props => (
      <div className="pluginWrapper buttonWrapper">
        <a className="button" href={props.href} target={props.target}>
          {props.children}
        </a>
      </div>
    );

    return (
      <SplashContainer>

        <div className="inner">
          <ProjectTitle siteConfig={siteConfig} />
          <PromoSection>
            <Button href={ docUrl('plugins/write-plugins') }>Write Plug-Ins</Button>
            <Button href={ docUrl('clients/clients-introduction') }>Write Clients</Button>
            <Button href={ docUrl('build/build-nymea') }>Build Nymea</Button>
          </PromoSection>
        </div>
      </SplashContainer>
    );
  }
}

class Index extends React.Component {
  render() {
    const {config: siteConfig, language = ''} = this.props;
    const {baseUrl} = siteConfig;

    const Block = props => (
      <Container
        padding={['bottom', 'top']}
        id={props.id}
        background={props.background}>
        <GridBlock
          align="center"
          contents={props.children}
          layout={props.layout}
        />
      </Container>
    );

    const Intro = () => (
      <div
        className="productShowcaseSection paddingBottom"
        style={{textAlign: 'center'}}>
        <h2>Open edge IoT middleware</h2>
        <MarkdownBlock>nymea is an open source IoT stack. Its main components are the core, the plugins and the client app. Do you want to enable your hardware to work with nymea? Plugin development is what you want. Do you want to create your user interface? Check out nymea:app as a reference implementation. Eager to extend the overall platform? Dive into core development!</MarkdownBlock>
      </div>
    );

    const TryOut = () => (
      <Block id="purpose">
        {[
          {
            content:
              'Devices that needs to be connected to other services or devices, some examples:' +
              ' Building automation' +
              ' Heating controller' +
              ' Irrigation or sprinkler system' +
              ' Access and alarm system' +
              ' Smart Home Hubs' +
              ' Audio device' +
              ' Hot tub or sauna' +
              ' Protocol adapter',
            image: `${baseUrl}img/help-buoy.svg`,
            imageAlign: 'left',
            title: 'nymea is built for connected devices',
          },
        ]}
      </Block>
    );

    const Description = () => (
      <Block background="believes">
        {[
          {
            content:
              'We think IoT devices, especially inside your home do not have to be cloud connected all the time.' +
              'Privacy is one of our concerns, so we help to build better cloud independent products. A product doesn’t' +
              'have be rendered worthless as soon as the manufacturer shuts down the cloud. We acknowledge that to keep the' +
              'devices up-to-date takes a lot of effort. Nymea is built to reduce this maintenance effort. There will be' +
              'still maintenance effort and the resulting costs must be sustainable. We support manufacturers to charge for' +
              'added value. Selling hardware was a main income for many manufacturers, we encourage for durable products not' +
              'only as benefit to the user but also in favor of our environment.' +
              ' ' +
              'The nymea Team',
            image: `${baseUrl}img/heart.svg`,
            imageAlign: 'right',
            title: 'Affair of the heart',
          },
        ]}
      </Block>
    );

    const LearnHow = () => (
      <Block background="light">
        {[
          {
            content:
              'nymea consists our of 3 components.',
            image: `${baseUrl}img/Software.svg`,
            imageAlign: 'right',
            title: 'nymea software stack',
          },
        ]}
      </Block>
    );

    const Features = () => (
      <Block layout="fourColumn">
        {[
          {
            content: 'The nymea core is main part of the whole stack and does the overall management. Check the docs for a detailed description on how it works and how to speak with it.',
            image: `${baseUrl}img/volume-high.svg`,
            imageAlign: 'top',
            title: 'Core Development',
          },
          {
            content: 'A plug-in\'s purpose is to handle the communication between nymea and the device or service. Everything else is provided by nymea like events, states, actions, logs, clients and API.',
            image: `${baseUrl}img/volume-medium.svg`,
            imageAlign: 'top',
            title: 'Plug-In Development',
          },
          {
            content: 'nymea:app is the community app for you to use or provide a starting point for creating your own nymea client.',
            image: `${baseUrl}img/volume-low.svg`,
            imageAlign: 'top',
            title: 'Client Development',
          },
        ]}
      </Block>
    );

    const Showcase = () => {
      if ((siteConfig.users || []).length === 0) {
        return null;
      }

      const showcase = siteConfig.users
        .filter(user => user.pinned)
        .map(user => (
          <a href={user.infoLink} key={user.infoLink}>
            <img src={user.image} alt={user.caption} title={user.caption} />
          </a>
        ));

      const pageUrl = page => baseUrl + (language ? `${language}/` : '') + page;

      return (
        <div className="productShowcaseSection paddingBottom">
          <h2>nymea Showcases</h2>  
          <p>This project is used for those projects</p>
          <div className="logos">{showcase}</div>
          <div className="more-users">
            <a className="button" href={pageUrl('users.html')}>
              More Showcases
            </a>
          </div>
        </div>
      );
    };

    return (
      <div>
        <HomeSplash siteConfig={siteConfig} language={language} />
        <div className="mainContainer">
          <Intro />
          <Features />
          <LearnHow />
          <TryOut />
          <Description />
          <Showcase />
        </div>
      </div>
    );
  }
}

module.exports = Index;
