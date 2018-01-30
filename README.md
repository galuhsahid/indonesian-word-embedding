# Indonesian Word Embedding
A web application that demonstrates Indonesian word embedding, inspired by [Word embedding demo](bionlp-www.utu.fi/wv_demo/).

See the demo: http://indonesian-word-embedding.herokuapp.com

Right now it serves pre-trained word vectors from [here](https://github.com/Kyubyong/wordvectors). The word vectors are trained on the Word2vec model from Wikipedia texts using the CBOW training algorithm. 

## 💡 future improvements
- **Refactoring**. This is my time using Vue so I'm sure there are a lot of things to be refactored that I haven't known yet!
- **Serves multiple models**. Not only Word2vec using CBOW but also Word2vec using skip-gram or even FastText.
- **Add more in-depth explanations**, possibly for each section.
- As more explanations are added, **consider using Vuex**.
- **Indonesian translation**.

## 💭 contribute
If you're interested to work in improving the points above or if you have any idea, feel free to make a pull request! 🙏

## ⚙ setup

``` bash
# install front-end
cd frontend
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production/Flask with minification
npm run build

# install back-end
cd ../backend
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
cd ..

# serve back-end at localhost:5000
FLASK_APP=run.py flask run
```

## credits
- [Web app boilerplate](https://github.com/oleg-agapov/flask-vue-spa)
- [Pre-trained word vectors](https://github.com/Kyubyong/wordvectors)