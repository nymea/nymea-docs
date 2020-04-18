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

    const SaveOnIntegration = () => (
      <Block id="purpose">
        {[
          {
            content:
              'Make your product work with anything.<br><br>Nymea is ready to extend connectivity of your IoT device to virtually anything. Adding new integrations is easily done via over-the-air updates.',
            image: `${baseUrl}img/nymea-integrations.png`,
            imageAlign: 'left',
            title: 'Save thousands of integration hours',
          },
        ]}
      </Block>
    );

    const Footprint = () => (
      <Block background="light">
        {[
          {
            content:
              'A powerful, yet lean addon for your device firmware.',
            image: `${baseUrl}img/nymea_vs_java_footprint.png`,
            imageAlign: 'right',
            title: 'The worlds smallest footprint',
          },
        ]}
      </Block>
    );

    const Hardware = () => (
      <Block>
        {[
          {
            content:
              'As reliable as a Swiss watch.<br><br>As flexible as a Swiss Army knife.',
            image: `${baseUrl}img/HW-SW-modules.png`,
            imageAlign: 'right',
            title: 'Also need hardware?',
          },
        ]}
      </Block>
    );

    const Partners = () => (
      <Block layout="fourColumn" background="light">
        {[
          {
            content: '',
            image: `${baseUrl}img/partners/marantec.png`,
            imageAlign: 'top',
            title: '',
          },
          {
            content: '',
            image: `${baseUrl}img/partners/streamunlimited.png`,
            imageAlign: 'top',
            title: '',
          },
          {
            content: '',
            image: `${baseUrl}img/partners/qt.png`,
            imageAlign: 'top',
            title: '',
          },
          {
            content: '',
            image: `${baseUrl}img/partners/ubuntu.png`,
            imageAlign: 'top',
            title: '',
          },
        ]}
      </Block>
    );

    const GetInTouch = () => {
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
          <h2>Get in touch</h2>  
          <p>Contact us to discuss opportunities, products and inquiries!</p>
          <div className="more-users">
            <a className="button" href={pageUrl('users.html')}>
              Let's talk
            </a>
          </div>
        </div>
      );
    };

    return (
      <div>
        <div className="mainContainer">
          <SaveOnIntegration />
          <Footprint />
          <Hardware />
          <Partners />
          <GetInTouch />
        </div>
      </div>
    );
  }
}

module.exports = Index;
