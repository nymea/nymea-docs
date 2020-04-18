/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// See https://docusaurus.io/docs/site-config for all the possible
// site configuration options.

// List of projects/orgs using your project for the users page.
const users = [
  {
    caption: 'nymea',
    // You will need to prepend the image path with your baseUrl
    // if it is not '/', like: '/test-site/img/image.jpg'.
    image: '/img/owl_white.svg',
    infoLink: 'https://nymea.io',
    pinned: true,
  },
];

const siteConfig = {
  title: 'nymea',
  tagline: 'IoT - Connectivity - Smart Home',
  url: 'https://nymea.io', // Your website URL
  baseUrl: '/', // Base URL for your project */


  // Used for publishing and more
  projectName: 'nymea',
  organizationName: 'nymea GmbH',

  // For no header links in the top nav bar -> headerLinks: [],
  headerLinks: [
    { page: 'quick-start', label: 'Quick Start' },
    { page: 'b2bservices', label: 'B2B services' },
    { page: 'developers', label: 'Developers' },
    { page: 'help', label: 'Help'},
    { blog: true, label: 'Blog' },   
    { search: true },
  ],

  // If you have users set above, you add it here:
  users,

  /* path to images for header/footer */
  headerIcon: 'img/owl_white.svg',
  footerIcon: 'img/owl_white.svg',
  favicon: 'img/owl_white.svg',

  /* Colors for website */
  colors: {
    primaryColor: '#69938c',
    secondaryColor: '#676767',
  },

  /* Custom fonts for website */

  fonts: {
    myFont: [
      "Ubuntu",
      "Serif"
    ],
    myOtherFont: [
      "-apple-system",
      "system-ui"
    ]
  },


  // This copyright info is used in /core/Footer.js and blog RSS/Atom feeds.
  copyright: `Copyright © ${new Date().getFullYear()} nymea GmbH`,

  highlight: {
    // Highlight.js theme to use for syntax highlighting in code blocks.
    theme: 'default',
  },

  // Add custom scripts here that would be placed in <script> tags.
  scripts: ['https://buttons.github.io/buttons.js'],

  // On page navigation for the current documentation page.
  onPageNav: 'separate',
  // No .html extensions for paths.
  cleanUrl: true,

  // Open Graph and Twitter card images.
  ogImage: 'img/undraw_online.svg',

  twitter: 'true',
  twitterImage: 'img/undraw_tweetstorm.svg',
  twitterUsername: 'nymea_io', 

  // For sites with a sizable amount of content, set collapsible to true.
  // Expand/collapse the links and subcategories under categories.
  docsSideNavCollapsible: true,

  // Show documentation's last contributor's name.
  // enableUpdateBy: true,

  // Show documentation's last update time.
  // enableUpdateTime: true,

  // You may provide arbitrary config keys to be used as needed by your
  // template. For example, if you need your repo's URL...
  repoUrl: 'https://github.com/nymea/nymea',
};

module.exports = siteConfig;
