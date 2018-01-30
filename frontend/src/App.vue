<template>
  <div id="app">
    <div id="left"></div>
    <h1 class="title">Indonesian Word Embedding</h1>
    <SimilarWords />
    <Similarity />
    <MostSimilarGiven />
    <WordPair />
    <DoesntMatch />
    <Footer />
  </div>
</template>

<script>
import DoesntMatch from './components/DoesntMatch'
import MostSimilarGiven from './components/MostSimilarGiven'
import Similarity from './components/Similarity'
import SimilarWords from './components/SimilarWords'
import WordPair from './components/WordPair'

import Footer from './components/Footer'
export default {
  name: 'app',
  components: {
    DoesntMatch,
    MostSimilarGiven,
    Similarity,
    SimilarWords,
    WordPair,
    Footer
  }
}
</script>

<style lang="scss">
  // Import Google Fonts
  @import url('https://fonts.googleapis.com/css?family=Cabin');

  // Import Bulma's core
  @import "~bulma/sass/utilities/_all";

  // Colors
  $body-background-color: #FFF1EE;
  $body-color: #060F46;
  $primary: #FF3543;
  $primary-invert: findColorInvert($primary);
  $secondary: #2852FF;
  $secondary-invert: findColorInvert($secondary);

  // Links
  $link: $primary;
  $link-invert: $primary-invert;
  $link-focus-border: $primary;

  // Font
  $family-primary: 'Cabin', sans-serif;

  // Import Bulma and Buefy styles
  @import "~bulma";
  @import "~buefy/src/scss/buefy";

  span {
    font-size: 1.5rem;
    font-weight: 700;
  }

  ul {
    text-align: center;
  }

  .button.how-it-works {
    color: $primary;
    border-color: transparent;
    text-align: center;
    padding: 10px;
  }

  .section.footer {
    background-color: transparent;
  }

  .note {
    padding: 10px;
  }
  
  #left {
    background: $secondary;
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    width: 15px;
    margin-right: 15px;
  }

  .empty-field {
    border-bottom: $primary solid 4px;
    min-width: 120px;
  }

  span.empty-field:empty:before {
    content: "\200b"; // unicode zero width space character
  }

  .title {
    color: $primary;
    padding: 50px;
    text-align: center;
  }

  .section {
    background-color: $white;
    border-radius: 5px;
    margin: 15px 30px;
  } 

  .result {
    color: $primary;
    font-weight: 700;
  }

</style>
