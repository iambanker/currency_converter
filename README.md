## Setup

## Example

## General

API uri

```
https://openexchangerates.org/api/
                                  latest.json
                                  currencies.json
                                  historical/2013-02-16.json

https://openexchangerates.org/api/latest.json?app_id=YOUR_APP_ID
```

### Sample output
```
{
    disclaimer: "https://openexchangerates.org/terms/",
    license: "https://openexchangerates.org/license/",
    timestamp: 1449877801,
    base: "USD",
    rates: {
        AED: 3.672538,
        AFN: 66.809999,
        ALL: 125.716501,
        AMD: 484.902502,
        ANG: 1.788575,
        AOA: 135.295998,
        ARS: 9.750101,
        AUD: 1.390866,
        /* ... */
    }
}
```

### Test

```
python -m pytest tests
```
