create table NflHistoricalOfficalPast3Years
(
    Game_ID            INTEGER not null primary key autoincrement,
    Season             INTEGER,
    Week               INTEGER,
    SeasonWeek_ID      VARCHAR(8),
    gameDate           DATE,
    FavoredTeam_ID     VARCHAR(20),
    Underdog_ID        VARCHAR(20),
    Winner_ID          VARCHAR(30),
    Game_Era           INTEGER,
    Fav_Implied_Win_P  INTEGER,
    UndD_Implied_Win_P INTEGER,
    American_Odds_Fav  VARCHAR(20),
    American_Odds_Und  VARCHAR(20),
    Dec_Odds_Fav       REAL,
    Dec_Odds_UndD      Float
);

INSERT INTO NflHistoricalOfficalPast3Years
SELECT *
FROM NflHistoricalOffical
WHERE Season >= 55;

DELETE FROM NflHistoricalOffical
WHERE Season >= 55;