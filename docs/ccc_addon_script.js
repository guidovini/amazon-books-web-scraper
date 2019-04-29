void function () {
    var e = location.href.search(/(amazon.|amzn.)(com|co\.uk|ca|de|fr|es|it|cn|co\.jp).+/i) >= 0,
        c = /amazon.(com|co\.uk|ca|de|fr|es|it|cn|co\.jp).*\/(asin|dp|gp|product|exec\/obidos|gp\/offer-listing|product\-reviews|gp\/aw\/d)\/[A-Z0-9]{10,13}/i,
        t = /amzn.(com|co\.uk|ca|de|fr|es|it|cn|co\.jp)\/[A-Z0-9]{10,13}/i,
        a = location.href.search(c) >= 0,
        o = location.href.search(/camelcamelcamel.com/i) >= 0,
        n = "ccc-injected-links-569DE51E-99CE-4ACE-BD10-7F85542A54A8",
        l = !(null == document.getElementById(n)),
        i = "0.2",
        m = "ctx_prid=5%26utm_campaign=bookmarklet%26v_camelet=" + i;
    if (a) try {
            var r = document.getElementById("ASIN").value;
            window.open("http://camelcamelcamel.com/search%3Fq=" + window.location.origin + "/dp/" + r + "%26" + m, "_blank")
        } catch (d) {
            window.open("http://camelcamelcamel.com/search%3Fq=" + encodeURIComponent(location.href) + "%26" + m, "_blank")
        } else if (l || e || o) window.open("http://camelcamelcamel.com/%3F" + m, "_self");
        else {
            var s = [];
            links = document.links;
            for (var h = 0; h < links.length; h++)(links[h].href.search(c) >= 0 || links[h].href.search(t) >= 0) && s.push(links[h]);
            for (var h = 0; h < s.length; h++) {
                for (var p = s[h].childNodes.length, f = !1, g = 0; p > g; g++) "img" != s[h].childNodes[g].nodeName.toLowerCase() || (f = !0);
                if (!f && "" != s[h].text) {
                    var u = document.createElement("a"),
                        w = document.createElement("img"),
                        k = document.createTextNode("%C2%A0");
                    w.src = "http://s3.camelcamelcamel.com/images/ccc.png", w.style.height = "0.8em", w.style.verticalAlign = "text-center", u.appendChild(w), u.title = "View Amazon price history at camelcamelcamel.com", u.target = "_blank", u.href = "http://www.camelcamelcamel.com/search%3Fq=" + s[h].href + "%26" + m, s[h].parentNode.insertBefore(u, s[h].nextSibling), s[h].parentNode.insertBefore(k, s[h].nextSibling)
                }
            }
            ccc_inj = document.createElement("div"), ccc_inj.id = n, document.body.insertBefore(ccc_inj, document.body.childNodes[0]), 0 == s.length && window.open("http://camelcamelcamel.com/%3F" + m, "_self")
        }
}();

// Problem with % 26 % 26 which is && due to web enconding. Check http://krypted.com/utilities/html-encoding-reference/