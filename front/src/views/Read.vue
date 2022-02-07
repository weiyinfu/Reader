<template>
  <div class="Read" ref="ele">

    <div class="header">
      <router-link to="/">回首页</router-link>
      <el-button @click="showCatalog = true" type="primary" style="margin-left: 16px;">
        目录
      </el-button>
    </div>
    <div class="article" v-if="content">
      <p v-for="(line,ind) in content.split('\n')" :key="ind">{{ line }}</p>
    </div>
    <div class="footer">
      <router-link :to="{
                path:'/Read',
                query:{
                    book:book.id,
                    article:prevArticle?.id,
                }
            }"
                   v-if="prevArticle?.name"
      >上一章：{{ prevArticle?.name }}
      </router-link>
      <router-link :to="{
                path:'/Read',
                query:{
                    book:book.id,
                    article:nextArticle?.id,
                }
            }"
                   v-if="nextArticle?.name"
      >下一章：{{ nextArticle?.name }}
      </router-link>
    </div>
    <el-drawer :with-header="false" v-model="showCatalog" direction="ltr" :before-close="hideCatalog">
      <book-catalog :book="book" v-if="book.name"></book-catalog>
    </el-drawer>
  </div>
</template>
<script>
import api from "../api.ts";
import BookCatalog from "../components/BookCatalog";

export default {
  components: {
    BookCatalog,
  },
  data() {
    return {
      content: '',
      book: {},
      articles: [],
      article: {},
      showCatalog: false,
    }
  },
  watch: {
    article() {
      document.title = `【${this.book.name}】${this.article.name}`;
    },
    "$route.query": function () {
      this.load();
    }
  },
  computed: {
    prevArticle() {
      const last = this.articles.indexOf(this.article) - 1;
      if (last >= 0) return this.articles[last];
      else return null;
    },
    nextArticle() {
      const next = this.articles.indexOf(this.article) + 1;
      if (next < this.articles.length) return this.articles[next];
      else return null;
    },
  },
  methods: {
    hideCatalog() {
      this.showCatalog = false;
    },
    load() {
      if (!this.$route.path === "/Read") {
        return;
      }
      if (!this.$route.query.book) {
        return;
      }
      document.querySelector(".Read").scrollTop = 0;
      api.getBook(this.$route.query.book).then(resp => {
        this.book = resp.data;
        const articles = [];
        let article = this.$route.query.article;

        for (let part of this.book.parts) {
          for (let art of part.articles) {
            articles.push(art);
          }
        }
        this.articles = articles;
        if (!article) {
          article = this.articles[0].id;
          this.showCatalog = true;
        }
        for (let art of this.articles) {
          if (art.id === article) {
            this.article = art;
          }
        }
        document.title = `【${this.book.name}】${this.article.name}`;

        api.getArticle(article).then(resp => {
          this.content = resp.data;
        })
      })
    }
  },
  mounted() {
    this.load();
  }
}
</script>
<style lang="less">
.Read {
  display: flex;
  align-items: center;
  /*justify-content: center;*/
  background: #3b2e2a;
  flex-direction: column;
  height: 100%;
  overflow: auto;

  .el-drawer {
    width: unset !important;
  }

  .article {
    max-width: 700px;
    background: #e1e1db;
    padding: 20px;
    border-radius: 10px;
    margin: 10px;
  }

  .article {
    max-width: 700px;
    background: #e1e1db;
    padding: 20px;
    border-radius: 10px;
    margin: 10px;
  }

  .header, .footer {
    a {
      color: white;
      text-decoration: none;
    }
  }

  .el-drawer__body {
    height: 100%;
    overflow: auto;
  }

  .Book {
    box-sizing: border-box;
    padding: 10px;
    width: fit-content;

    .category-item {
      font-size: 15px;
    }

    .author {
      font-style: italic;
      font-size: 14px;
    }

    .tag {
      border-radius: 10px;
      background: #fDf6f8;
      padding: 5px;
      font-size: 10px;
    }
  }
}

</style>