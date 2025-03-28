"""
Data from https://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2025&MONTH=03&FROM=2812&TO=2812&STNM=72451
72451 DDC Dodge City(Awos) Observations at 12Z 28 Mar 2025
"""

import pandas

data2025Mar28 = pandas.DataFrame(
    data=(
        (790, 13.6),
        (920, 14.0),
        (1014, 13.2),
        (1080, 13.4),
        (1156, 15.4),
        (1195, 15.2),
        (1362, 15.8),
        (1451, 15.4),
        (1461, 15.4),
        (1511, 15.3),
        (1766, 14.8),
        (1901, 13.9),
        (1986, 13.4),
        (2188, 12.3),
        (2318, 11.6),
        (2340, 11.4),
        (2439, 11.2),
        (2583, 10.2),
        (2890, 8.2),
        (3076, 6.6),
        (3337, 4.8),
        (3666, 2.0),
        (3754, 1.2),
        (3766, 1.2),
        (4451, -4.2),
        (4491, -4.5),
        (4804, -7.1),
        (4944, -8.3),
        (5042, -9.1),
        (5199, -10.3),
        (5228, -10.5),
        (5329, -11.5),
        (5730, -15.1),
        (5806, -15.7),
        (5882, -16.5),
        (5943, -17.0),
        (5974, -17.3),
        (6036, -17.7),
        (6098, -17.9),
        (6114, -17.9),
        (6145, -18.1),
        (6193, -18.5),
        (6272, -19.3),
        (6400, -20.5),
        (6449, -20.7),
        (6497, -21.1),
        (6530, -21.3),
        (6579, -21.7),
        (6612, -21.9),
        (6645, -22.3),
        (6695, -22.5),
        (6712, -22.5),
        (6728, -22.5),
        (6745, -22.7),
        (6812, -22.9),
        (6829, -22.9),
        (6880, -23.3),
        (7018, -24.3),
        (7122, -24.9),
        (7227, -25.7),
        (7281, -26.1),
        (7370, -26.9),
        (7424, -27.3),
        (7553, -28.3),
        (7776, -30.3),
        (7947, -31.9),
        (8044, -32.7),
        (8161, -33.5),
        (8220, -33.9),
        (8320, -34.9),
        (8340, -35.1),
        (8440, -35.5),
        (8708, -37.9),
        (8897, -39.5),
        (9005, -39.7),
        (9335, -42.1),
        (9380, -42.3),
        (9493, -43.1),
        (9679, -44.3),
        (10590, -52.1),
        (10773, -53.5),
        (10852, -54.1),
        (11521, -59.1),
        (11638, -59.5),
        (12000, -62.5),
        (12187, -64.0),
        (12219, -64.3),
        (12315, -64.2),
        (12646, -63.7),
        (12749, -61.5),
        (12784, -60.7),
        (12855, -60.9),
        (12964, -58.9),
        (13037, -59.2),
        (13536, -61.5),
        (13780, -60.1),
        (14035, -58.9),
        (14167, -58.6),
        (14212, -58.5),
        (14767, -60.5),
        (15272, -62.3),
        (15651, -63.7),
        (16290, -63.7),
        (16604, -63.8),
        (16800, -63.9),
        (16962, -63.9),
        (17003, -64.2),
        (17205, -65.5),
        (17212, -65.5),
        (17578, -64.4),
        (17967, -63.2),
        (18048, -63.0),
        (18155, -62.7),
        (18213, -63.0),
        (18470, -64.5),
        (18557, -64.7),
        (19015, -66.0),
        (19287, -66.7),
        (19510, -65.7),
        (19827, -64.3),
        (19926, -63.9),
        (19937, -63.9),
        (20280, -64.4),
        (20520, -64.7),
        (20532, -64.9),
        (20900, -62.6),
        (21085, -61.5),
        (21167, -61.4),
        (21307, -61.2),
        (21745, -60.7),
        (21898, -60.5),
        (22216, -60.2),
        (22282, -60.1),
        (22535, -61.1),
        (22727, -60.8),
        (22907, -60.5),
        (23111, -60.1),
        (23285, -58.6),
        (23384, -57.7),
        (23690, -58.7),
        (23902, -59.0),
        (24121, -59.4),
        (24755, -60.3),
        (24830, -60.0),
        (25357, -57.7),
        (26240, -53.9),
        (26571, -53.0),
        (27177, -51.3),
        (27764, -53.1),
        (28102, -52.2),
        (29032, -49.6),
        (29236, -49.1),
        (29721, -50.1),
        (30125, -49.5),
        (30620, -48.7),
        (30750, -49.1),
        (31088, -46.3),
        (31596, -44.9),
        (32230, -45.3),
        (32571, -45.5),
        (32749, -44.1),
        (33025, -45.1),
        (33120, -43.9),
        (33415, -42.9),
    ),
    columns=("height", "temperature [C]"),
)
