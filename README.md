# API DOCS

## Endpoints

### GET

1. **/news-map**:
    ```
    {
        "country" (2 letter ISO)
        "num_stories"
        "last_updated_on"
    }
    ```

2. **/news-map/{country_iso}**
    ```
    [
        {
            "id",
            "headline",
            "sentiment",
            "url"
        }
    ]
    ```

3. **/news-article/{article_id}**
```
{
    "headline",
    "description",
    "ml_summary",
    "url"
}
```
