DELETE FROM NflHistoricalOffical;

UPDATE NflHistoricalOffical
SET SeasonWeek_ID = (Season + (Week / 100.00));

UPDATE spreadspoke_scores
SET schedule_week = (SELECT MAX(schedule_week) + 1 WHERE schedule_season = 1967)
WHERE schedule_week = 'Conference';

UPDATE NflHistoricalOffical
SET SeasonWeek_ID = SeasonWeek_ID || 'p'
FROM spreadspoke_scores
JOIN spreadspoke_scores ON
WHERE schedule_playoff = TRUE;

UPDATE spreadspoke_scores
SET Game_ID = n.Game_ID
FROM spreadspoke_scores s JOIN NflHistoricalOffical n on 1 = 1;


ALTER TABLE spreadspoke_scores
DROP COLUMN Game_ID;

ALTER TABLE spreadspoke_scores
ADD COLUMN Game_ID INTEGER AUTO_INCREMENT;



CREATE VIEW spreadspoke_scores_gameID
AS
SELECT ROW_NUMBER() OVER() AS num_row, *
FROM spreadspoke_scores;

SELECT * FROM spreadspoke_scores_gameID;

ALTER TABLE spreadspoke_scores_gameID
DROP COLUMN Game_ID;

SELECT COUNT(*) FROM spreadspoke_scores_gameID;
DELETE FROM NflHistoricalOffical;

WITH RECURSIVE
    for(i) AS (VALUES(1) UNION ALL SELECT I+1 FROM for WHERE i < 13517)
INSERT INTO NflHistoricalOffical (Game_ID, Season, Week, gameDate, FavoredTeam_ID, Winner_ID, Game_Era)
       SELECT num_row, schedule_season-1965, schedule_week, schedule_date, team_favorite_id, winning_team, (((schedule_season / 10) % 10) + ((schedule_season / 1000) * 10) - 10)
        FROM spreadspoke_scores_gameID;

UPDATE NflHistoricalOffical
SET Season = (SELECT schedule_season - 1965
              FROM spreadspoke_scores_gameID);

UPDATE NflHistoricalOffical
SET UndD_Implied_Win_P = round(1 - Fav_Implied_Win_P, 2);

UPDATE NflHistoricalOffical
SET SeasonWeek_ID = Season || '.' || Week;

SELECT DISTINCT (team_away) FROM spreadspoke_scores;

UPDATE NflHistoricalOffical
SET Winner_ID = 'Tennessee Titans'
WHERE Winner_ID = 'Tennessee Oilers'


SELECT DISTINCT (Winner_ID) FROM NflHistoricalOffical;

UPDATE NflHistoricalOffical
SET Winner_ID = (SELECT Winner_ID w WHERE w.Game_ID = NflHistoricalOffical.Game_ID + 1)


UPDATE NflHistoricalOffical
SET Winner_ID = t2.Winner_ID
FROM NflHistoricalOffical AS t1
JOIN NflHistoricalOffical AS t2
ON t2.Game_ID=t1.Game_ID+1
WHERE t1.Game_ID<=13515;
