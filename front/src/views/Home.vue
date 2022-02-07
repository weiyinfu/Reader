<template>
    <div class="Home">
        <div>
            <div class="book" v-for="book in books" :key="book.name">

                <router-link :to="{
                path:'/Read',query:{'book':book.id}
            }">{{book.name}}
                </router-link>
                <span class="author">{{book.author}}</span>
                <span class="tag"
                      v-for="tag in book.tags" :key="tag">{{tag}}</span>
            </div>
        </div>
    </div>
</template>

<script>
    import api from "../api.ts";
    export default ({
        data() {
            return {books: []}
        },
        mounted() {
            api.getBookList().then(resp => {
                this.books = resp.data;
            })
        },
        methods: {}
    });
</script>
<style lang="less">
    .Home {
        display: flex;
        align-items: center;
        flex-direction: column;

        .book {
            font-weight: bold;
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
</style>
