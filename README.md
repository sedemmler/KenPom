# KenPom

A quick and dirty way to pull various cuts of data from the incredible NCAA Basketball advanced stats website KenPom.

What does it do?

(1) Quickly scrape the entire main page at KenPom into a Pandas DataFrame.
```
kenny = KenPom(start=2002, end=2003)
kenny.df

        Rk                 Team  Conf Record  ...   OppO   OppD  NCOS AdjEM  Season
0      1.0             Kentucky   SEC   32-4  ...  108.6   97.4        6.77    2003
1      2.0               Kansas   B12   30-8  ...  108.6   96.8        6.07    2003
2      3.0           Pittsburgh    BE   28-5  ...  105.5   98.4       -8.24    2003
3      4.0              Arizona   P10   28-4  ...  107.2   98.5        8.19    2003
4      5.0             Illinois   B10   25-7  ...  105.8   98.5       -4.18    2003
```

(2) Pull a specific team's historical main page stats

```
kenny = KenPom(start=2002, end=2003)
kenny.team('Duke')

Rk  Team Conf Record  AdjEM  ...  SoS AdjEM   OppO  OppD  NCOS AdjEM  Season
5  6.0  Duke  ACC   26-7  23.75  ...       8.85  107.1  98.3        0.64    2003
0  1.0  Duke  ACC   31-4  34.19  ...       9.87  109.1  99.2        6.66    2002
```

(3) Pull a specific conference's historical main page stats

```
kenny = KenPom(start=2002, end=2003)
kenny.conference('WAC')

idx     Rk            Team Conf Record  ...   OppO   OppD  NCOS AdjEM  Season
52    51.0           Tulsa  WAC  23-10  ...  102.7  101.7        4.16    2003
86    83.0          Nevada  WAC  17-14  ...  103.2  100.9        4.98    2003
101   98.0      Fresno St.  WAC   20-8  ...  101.3  102.1       -1.87    2003
115  112.0            Rice  WAC  17-10  ...  101.0  101.0       -0.21    2003
118  115.0          Hawaii  WAC  19-12  ...  103.4  102.1       -1.42    2003
```

(4) Hone in on a single season across all teams

```
kenny = KenPom(start=2002, end=2020)
kenny.season(2002)

idx     Rk                 Team  Conf Record  ...   OppO   OppD  NCOS AdjEM  Season
0      1.0                 Duke   ACC   31-4  ...  109.1   99.2        6.66    2002
1      2.0           Cincinnati  CUSA   31-4  ...  106.3   99.7        3.48    2002
2      3.0             Maryland   ACC   32-4  ...  109.1   99.3        1.62    2002
3      4.0               Kansas   B12   33-4  ...  110.3   99.6        8.32    2002
4      5.0             Oklahoma   B12   31-5  ...  109.0  100.2       -0.45    2002
```