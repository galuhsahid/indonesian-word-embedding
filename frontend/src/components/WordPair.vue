<template>
  <section class="section">
    <div class="container">

      <div class="level">

        <div class="level-item">
          <b-input v-model="word1" placeholder="first word"></b-input>
        </div>

        <div class="level-item">
          <span>is to</span>
        </div>

        <div class="level-item">
          <b-input v-model="word2" placeholder="second word"></b-input>
        </div>

        <div class="level-item">
          <span>like</span>
        </div>

        <div class="level-item">
          <b-input v-model="word3" placeholder="third word"></b-input>
        </div>

        <div class="level-item">
          <span>is to</span>
        </div>

        <div class="level-item">
          <span v-if="wordPair" class="result">{{ wordPair }}</span>
          <span v-else class="empty-field"></span>
        </div>
      </div>

      <div class="level">
        <div class="level-left">
          <div class="level-item">
            <b-collapse :open="false">
                <button class="button how-it-works" slot="trigger">How does this work?</button>
                <div class="note">
                    <div class="content">
                        <p>
                            In word embeddings, we can figure out analogies through the difference between word vectors. <br />
                            The most famous one is probably the <strong>king - man + woman = queen</strong> analogy, which is another way to express that <strong>king is to man like queen is to woman</strong>. <br />
                            There are plenty examples as well, such as <strong>France - Paris</strong> and <strong>Japan - Tokyo</strong>.<br />
                            However, this depends on the quality of the word embedding trained; it may not work particularly well on certain data.
                        </p>
                    </div>
                </div>
            </b-collapse>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script src="https://cdn.jsdelivr.net/npm/lodash@4.13.1/lodash.min.js"></script>
<script>
import axios from 'axios'
import _ from 'lodash'
export default {
  data () {
    return {
      word1: '',
      word2: '',
      word3: '',
      wordPair: ''
    }
  },
  watch: {
    word1: function (newWord1, oldWord1) {
      this.getWordPair()
    },
    word2: function (newWord2, oldWord2) {
      this.getWordPair()
    },
    word3: function (newWord2, oldWord2) {
      this.getWordPair()
    }
  },
  methods: {
    getWordPair: _.debounce(
      function () {
        let params = {}
        params['word_1'] = this.word1
        params['word_2'] = this.word2
        params['word_3'] = this.word3
        const path = process.env.API_URL + `/word_pair`
        axios.get(path, {
          params: params
        })
        .then(response => {
          this.wordPair = response.data.wordPair
        })
        .catch(error => {
          this.wordPair = ''
          console.log(error)
        })
      },
      500
    )
  }
}
</script>
