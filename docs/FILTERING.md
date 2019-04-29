
## Filtering

Filter Amazon URL using regular expressions:

```regex
(amazon.|amzn.)(com|co\.uk|ca|de|fr|es|it|cn|co\.jp).+
```

```regex
amazon.(com|co\.uk|ca|de|fr|es|it|cn|co\.jp).*\/(asin|dp|gp|product|exec\/obidos|gp\/offer-listing|product\-reviews|gp\/aw\/d)\/[A-Z0-9]{10,13}
```

```regex
amzn.(com|co\.uk|ca|de|fr|es|it|cn|co\.jp)\/[A-Z0-9]{10,13}
```

**This**
```regex
(amazon.|amzn.)(com|co\.uk|ca|de|fr|es|it|cn|co\.jp).*\/(asin|dp|gp|product|exec\/obidos|gp\/offer-listing|product\-reviews|gp\/aw\/d)\/([A-Z0-9]{10,13})
```