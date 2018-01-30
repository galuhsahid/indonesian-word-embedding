<template>
  <section class="section">
    <div class="container">
      
      <div class="level">
        <div class="level-item">
          <span>The most similar word to</span>
        </div>

        <div class="level-item">
          <b-input v-model="word" placeholder="word"></b-input>
        </div>

        <div class="level-item">
          <span>given the words</span>
        </div>

        <div class="level-item">
          <b-taginput
              v-model="given"
              icon="label"
              placeholder="add a word">
          </b-taginput>
        </div>

        <div class="level-item">
          <span>is</span>
        </div>

        <div class="level-item">
          <span v-if="mostSimilar" class="result">{{ mostSimilar }}</span>
          <span v-else class="empty-field"></span>
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
      word: '',
      given: []
    }
  },
  watch: {
    word: function (newWord, oldWord) {
      this.getMostSimilar()
    },
    given: function (newGiven, oldGiven) {
      this.getMostSimilar()
    }
  },
  methods: {
    getMostSimilar: _.debounce(
      function () {
        let params = {}
        params['word'] = this.word
        params['given'] = this.given
        const path = process.env.API_URL + `/similar_to_given`
        axios.get(path, {
          params: params
        })
        .then(response => {
          this.mostSimilar = response.data.mostSimilar
        })
        .catch(error => {
          this.mostSimilar = ''
          console.log(error)
        })
      },
      500
    )
  }
}
</script>
