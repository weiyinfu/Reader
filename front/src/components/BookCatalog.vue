<template>
    <div class="Book">
        <h1>{{book.name}}</h1>
        <span class="author">{{book.author}}</span>
        <span class="tag" v-for="tag in book.tags" :key="tag">{{tag}}</span>
        <div class="part" v-for='part in book.parts' :key="part.name">
            {{part.name}}
            <div class="category-item" v-for="(article,ind) in part.articles" :key="ind">
                <router-link :to="{
                    path:'/Read',
                    query:{
                        article:article.id,
                        book:book.id,
                    }
                }">{{article.name}}
                </router-link>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        props: {
            book: {
                type: Object,
                required: true,
            }
        },
        data() {
            return {}
        },
        mounted() {

        }
    }
</script>