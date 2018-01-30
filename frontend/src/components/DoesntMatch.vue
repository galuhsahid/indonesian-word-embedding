<template>
  <section class="section">
    <div class="container">
      
      <div class="level">
        <div class="level-item">
          <span>The word that does not belong in</span>
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
          <span v-if="doesntMatch" class="result">{{ doesntMatch }}</span>
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
    given: function (newGiven, oldGiven) {
      this.getDoesntMatch()
    }
  },
  methods: {
    getDoesntMatch: _.debounce(
      function () {
        let params = {}
        params['given'] = this.given
        const path = process.env.API_URL + `/doesnt_match`
        axios.get(path, {
          params: params
        })
        .then(response => {
          this.doesntMatch = response.data.doesntMatch
        })
        .catch(error => {
          console.log(error)
        })
      },
      500
    )
  }
}
</script>
