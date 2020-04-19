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
    console.log("***");
    console.log(this.props);
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
            <Button href={ docUrl('about/overview') }>About nymea</Button>
            <Button href={ docUrl('users/installation/gettingstarted') }>Users guide</Button>
            <Button href={ docUrl('developers/introduction') }>Developers guide</Button>
            <Button href={ './b2bservices' }>B2B services</Button>
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
        <MarkdownBlock>nymea is an open source IoT stack. It is used to build smart IoT devices, smart home gateways or enable individual IoT related features in connected products. We follow a \"local first\" approach, which means nymea will keep users data private and will still be functional even without Internet connection. Obviously, cloud integration is still available if wanted.</MarkdownBlock>
      </div>
    );

    const TryOut = () => (
      <Block id="purpose" background="light">
        {[
          {
            content:
              'Connect lighting, media, heatings, irrigations and sprinklers, garage doors, alarm systems and many more to a centralized, local and privacy focused control center with nymea. Or build your device running nymea to connect and integrate with other solutions, such as Alexa or Google Home.',
            image: `${baseUrl}img/nymea-integrations.png`,
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
              'We think that IoT devices, especially inside your home do not have to be cloud connected all the time. ' +
              'Privacy and reliability are our main concerns. With that in mind we build anything we do with a offline-first approach. ' +
              'This results in blazing fast reaction times, full control over personal data and guarantees your product won\'t be rendered ' +
              'useless if the cloud provider you\'ve been betting on shuts down their service. <br> ' +
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
      <Block>
        {[
          {
            content:
              'Simple, yet powerful.<br><br>The nymea core stack is written in C++ and Qt. This results in low hardware requirements and high performance. To ease and speed up development time, individual integrations and automation behaviours can be added with JavaScript.',
            image: `${baseUrl}img/Software.svg`,
            imageAlign: 'right',
            title: 'The nymea software stack',
          },
        ]}
      </Block>
    );

    const Features = () => (
      <Block layout="fourColumn" background="light">
        {[
          {
            content: 'nymea gets you up and running with your smart home setup in no time. Just install nymea:core and nymea:app and you\'re all set with a powerful smart home solution that does not require powerful hardware or fiddling with cryptic configuration files. Using 100% free and open source software.',
            image: `${baseUrl}img/users.svg`,
            imageAlign: 'top',
            title: 'For users',
          },
          {
            content: 'When you\'re building your own IoT device, nymea will help with all the software efforts. Whether it\'s connecting your device to others, adding easy set-up features, creating smart hubs for for all your devices or adding control and setup frontends, nymea\'s got your back.',
            image: `${baseUrl}img/developers.svg`,
            imageAlign: 'top',
            title: 'For developers',
          },
          {
            content: 'Building IoT enabled customer grade products can be hard. We\'ve ramped up with all the required know-how and with the nymea stack we\'ll be supporting your business. Whether it\'s fast prototyping and consulting, providing needed components, building entire products or caring for deployments and updates. Together with our partners we offer in-field experience for all of those aspects.',
            image: `${baseUrl}img/businesses.svg`,
            imageAlign: 'top',
            title: 'For businesses',
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
