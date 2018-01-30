<template>
  <section class="section">
    <div class="container">

        <div class="level">
            <div class="level-item">
                <span>Top</span>
            </div>
            <div class="level-item">
                <b-field>
                    <b-select
                        size="is-medium"
                        v-model="n"
                        >
                        <option value="5">5</option>
                        <option value="10">10</option>
                        <option value="20">20</option>
                    </b-select>
                </b-field>
            </div>
            <div class="level-item">
                <span>most similar words to</span>
            </div>
            <div class="level-item">
                <b-input v-model="word" placeholder="word"></b-input>
            </div>
            <div class="level-item">
                <span>are</span>
            </div>
        </div>

            <ul>
                <li v-for="item in similarWords">
                    <span>{{ item[0] }} (</span> <span class="result">{{  item[1] }}</span> <span>)</span>
                </li>
            </ul>
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
      isPublic: true,
      word: '',
      n: '',
      similarWords: ''
    }
  },
  watch: {
    word: function (newWord, oldWord) {
      this.getSimilarWords()
    },
    n: function (newN, oldN) {
      this.getSimilarWords()
    }
  },
  methods: {
    getSimilarWords: _.debounce(
      function () {
        let params = {}
        params['word'] = this.word
        params['n'] = this.n
        const path = process.env.API_URL + `/similar_word`
        axios.get(path, {
          params: params
        })
        .then(response => {
          this.similarWords = response.data.similarWords
        })
        .catch(error => {
          this.similarWords = ''
          console.log(error)
        })
      },
      500
    )
  }
}
</script>
