import axios from "axios";
import * as lib from "./lib";


export const cli = axios.create()

export function camelCase(resp: any) {
    resp.data = lib.camelCase(resp.data);
    return resp;
}


cli.interceptors.request.use(function (config: any) {
    // Do something before request is sent
    if (config.url.startsWith("/api")) {
        if (location.pathname.startsWith("/Reader/")) {
            //it's server
            config.url = `/Reader${config.url}`
        }
    }
    return config;
}, function (error) {
    // Do something with request error
    return Promise.reject(error);
})

interface Api {
    getBook(bookId: string): Promise<any>

    getArticle(article: string): Promise<any>

    getBookList(): Promise<any>
}

class BackendApi implements Api {
    getBook(bookId: string) {
        return cli.get("/api/book_info", {
            params: {
                book_id: bookId,
            }
        })
    }

    getArticle(article: any) {
        return cli.get("/api/get_article", {
            params: {
                article: article,
            }
        })
    }

    getBookList() {
        return cli.get("/api/book_list");
    }
}

class FileApi implements Api {
    getArticle(article: string): Promise<any> {
        if (!article) {
            throw new Error("getArticle article error")
        }
        return cli.get(`gen/${article}`)
    }

    getBook(bookId: string): Promise<any> {
        if (!bookId) {
            throw new Error("getbook bookId error")
        }
        return cli.get(`gen/${bookId}`);
    }

    getBookList(): Promise<any> {
        return cli.get(`gen/books`)
    }
}

export default new FileApi();