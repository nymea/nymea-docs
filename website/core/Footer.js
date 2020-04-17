/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

const React = require('react');

class Footer extends React.Component {
  docUrl(doc, language) {
    const baseUrl = this.props.config.baseUrl;
    const docsUrl = this.props.config.docsUrl;
    const docsPart = `${docsUrl ? `${docsUrl}/` : ''}`;
    const langPart = `${language ? `${language}/` : ''}`;
    return `${baseUrl}${docsPart}${langPart}${doc}`;
  }

  pageUrl(doc, language) {
    const baseUrl = this.props.config.baseUrl;
    return baseUrl + (language ? `${language}/` : '') + doc;
  }

  render() {
    return (
      <footer className="nav-footer" id="footer">
        <section className="sitemap">
          <a href={this.props.config.baseUrl} className="nav-home">
            {this.props.config.footerIcon && (
              <img
                src={this.props.config.baseUrl + this.props.config.footerIcon}
                alt={this.props.config.title}
                width="66"
                height="58"
              />
            )}
          </a>
          <div>
            <h5><a href={ this.pageUrl('quick-start', this.props.language) }>Quick Start</a></h5>
            <ul>
              <li><a href={ this.pageUrl('quick-start', this.props.language) }>Installation</a></li>
              <li><a href={ this.pageUrl('quick-start', this.props.language) }>Supported Devices</a></li>
              <li><a href={ this.pageUrl('quick-start', this.props.language) }>Supported Services</a></li>
            </ul>
          </div>
          <div>
            <h5><a href={ this.pageUrl('users', this.props.language) }>Users</a></h5>
            <ul>
              <li><a href={ this.pageUrl('users', this.props.language) }>App</a></li>
              <li><a href={ this.pageUrl('users', this.props.language) }>Configuration</a></li>
              <li><a href={ this.pageUrl('users', this.props.language) }>Services</a></li>
            </ul>            
          </div>
          <div>
            <h5><a href={ this.pageUrl('developers', this.props.language) }>Developers</a></h5>
            <ul>
              <li><a href={ this.docUrl('plugins/write-plugins') }>Write Plug-Ins</a></li>
              <li><a href={ this.docUrl('clients/clients-introduction') }>Write Clients</a></li>
              <li><a href={ this.docUrl('build/build-nymea') }>Build Nymea</a></li>
            </ul>
          </div>
          <div>
            <h5><a href="#">Community</a></h5>
            <ul>
              <li><a href="https://forum.nymea.io/">Forum</a></li>
              <li><a href="https://t.me/nymeacommunity">Telegram</a></li>
              <li><a href="https://discordapp.com/channels/652494572298960926/652494572298960929">Discord</a></li>
            </ul>
          </div>
          <div>
            <h5><a href="#">More</a></h5>
            <ul>
              <li><a href={`${this.props.config.baseUrl}blog`}>Blog</a></li>
              <li><a href="https://github.com/">GitHub</a></li>
              <li>
                <a className="github-button"
                  href={this.props.config.repoUrl}
                  data-icon="octicon-star"
                  data-count-href="/nymea/nymea/stargazers"
                  data-show-count="true"
                  data-count-aria-label="# stargazers on GitHub"
                  aria-label="Star this project on GitHub">Star</a>
              </li>
              <li>
                {this.props.config.twitterUsername && (
                  <div className="social">
                    <a
                      href={`https://twitter.com/${this.props.config.twitterUsername}`}
                      className="twitter-follow-button">
                      Follow @{this.props.config.twitterUsername}
                    </a>
                  </div>
                )}
                {this.props.config.facebookAppId && (
                  <div className="social">
                    <div
                      className="fb-like"
                      data-href={this.props.config.url}
                      data-colorscheme="dark"
                      data-layout="standard"
                      data-share="true"
                      data-width="225"
                      data-show-faces="false"
                    />
                  </div>
                )}
              </li>
            </ul>
          </div>
        </section>

        <section className="copyright">{this.props.config.copyright}</section>
      </footer>
    );
  }
}

module.exports = Footer;
