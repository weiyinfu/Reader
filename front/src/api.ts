import axios from "axios";
import * as lib from "./lib";


export const cli = axios.create()

export function camelCase(resp: any) {
    resp.data = lib.camelCase(resp.data);
    return resp;
}

interface Api {
    getBook(bookId: string): Promise<any>

    getArticle(article: string): Promise<any>

    getBookList(): Promise<any>
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