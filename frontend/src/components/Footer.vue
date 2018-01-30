<template>
  <section class="section footer">
    <div class="container">
      
      <div class="level">
        <div class="level-item">
          <span>by <a href="http://galuh.me">Galuh Sahid</a>. <a href="http://github.com/galuhsahid/indonesian-word-embedding">View source</a>.</span>
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
        const path = `http://localhost:5000/api/similarity`
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
