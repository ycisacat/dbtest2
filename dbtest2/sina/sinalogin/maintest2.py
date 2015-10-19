#coding=utf-8

"gsid_CTandWM的cookie属性:4u2V6b891MGbLgFyQffjhnLede5"

import cn.edu.hfut.dmic.webcollector.crawler.BreadthCrawler
import cn.edu.hfut.dmic.webcollector.model.Page
import cn.edu.hfut.dmic.webcollector.util.Config
import java.io.IOException
import org.jsoup.nodes.Element
import org.jsoup.select.Elements

class WeiboCrawler extends BreadthCrawler {

    public WeiboCrawler() {
        setUseragent("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0");
        setCookie("gsid_CTandWM=你的gsid_CTandWM;");
    }

    @Override
    public void visit(Page page) {
        Elements divs = page.getDoc().select("div.c");
        for (Element div : divs) {
            System.out.println(div.text());
        }
    }

    public static void main(String[] args) throws IOException, Exception {
        Config.topN = 0;
        WeiboCrawler crawler=new WeiboCrawler();

        for (int i = 1; i <= 10; i++) {
            crawler.addSeed("http://weibo.cn/u/1708942053?page=" + i);
        }
        crawler.addRegex(".*");
        crawler.setThreads(2);
        crawler.start(1);

    }
}
