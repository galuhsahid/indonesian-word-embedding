<template>
  <section class="section">
    <div class="container">
      
      <div class="level">
        <div class="level-item">
          <span>The similarity between</span>
        </div>

        <div class="level-item">
          <b-input v-model="word1" placeholder="first word"></b-input>
        </div>

        <div class="level-item">
          <span>and</span>
        </div>

        <div class="level-item">
          <b-input v-model="word2" placeholder="second word"></b-input>
        </div>

        <div class="level-item">
          <span>is</span>
        </div>

        <div class="level-item">
          <span v-if="similarity" class="result">{{ similarity }}</span>
          <span v-else class="empty-field"></span>
        </div>
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
                          To calculate the similarity between two words, we can measure the <strong>cosine similarity</strong> between the vectors representing each of the word.<br />
                          The cosine similarity falls is in the range between <strong>-1 to 1</strong>. <br />
                          A cosine similarity of 1 means the vectors are identical whereas -1 means the vectors are of opposite directions.<br />
                          We can expect relevant words to have a larger cosine similarity value compared to two irrelevant words.<br />
                      </p>
                  </div>
              </div>
          </b-collapse>
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
      similarity: ''
    }
  },
  watch: {
    word1: function (newWord1, oldWord1) {
      this.getSimilarity()
    },
    word2: function (newWord2, oldWord2) {
      this.getSimilarity()
    }
  },
  methods: {
    getSimilarity: _.debounce(
      function () {
        let params = {}
        params['word_1'] = this.word1
        params['word_2'] = this.word2
        const path = process.env.API_URL + `/similarity`
        axios.get(path, {
          params: params
        })
        .then(response => {
          this.similarity = response.data.similarity
        })
        .catch(error => {
          this.similarity = ''
          console.log(error)
        })
      },
      500
    )
  }
}
</script>
