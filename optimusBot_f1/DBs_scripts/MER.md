MER

![image](https://user-images.githubusercontent.com/22028539/123632415-47b27c80-d7ee-11eb-9594-3016ba61a4b8.png)

This MER will be used as structure to receive imported data from diferetn sources.

Script used to MER creation:

    CREATE TABLE circuits (circuitid INT(11), circuitRef VARCHAR(255), name VARCHAR(255), location VARCHAR(255), country VARCHAR(255), lat FLOAT, lng FLOAT, alt INT(11), url varchar(255));
    CREATE TABLE drivers (driverid INT(11), driverRef VARCHAR(255), number INT(11), code VARCHAR(3), forename VARCHAR(255), surname VARCHAR(255), dob DATE, nationality VARCHAR(255), url varchar(255));
    CREATE TABLE constructors (constructorid int(11), constructorRef VARCHAR(255), name VARCHAR(255), nationality VARCHAR(255), url VARCHAR(255));
    CREATE TABLE results (resultid INT(11), raceid INT(11), driverid INT(11), constructorid INT(11), number INT(11), grid INT(11), position INT(11), positionText VARCHAR(255), positionOrder INT(11), points FLOAT, laps INT(11), time VARCHAR(255), miliseconds INT(11), fastestLap INT(11), rank INT(11), fastaestLapTime VARCHAR(255), fastestLapSpeed VARCHAR(255), statusid INT(11));
    CREATE TABLE constructorResults (constructorResultId INT(11), raceid INT(11), constructorid INT(11), points FLOAT, status VARCHAR(255));
    CREATE TABLE races (raceid INT(11), year INT(11), round INT(11), circuitid FLOAT, name VARCHAR(255), date DATE, time TIME, url VARCHAR(255));

    ALTER TABLE circuits ADD PRIMARY KEY (circuitid);
    ALTER TABLE drivers ADD PRIMARY KEY (driverid);
    ALTER TABLE constructors ADD PRIMARY KEY (constructorid);
    ALTER TABLE results ADD PRIMARY KEY (resultid);
    ALTER TABLE constructorResults ADD PRIMARY KEY (constructorResultId);
    ALTER TABLE races ADD PRIMARY KEY (raceid);

    ALTER TABLE races ADD CONSTRAINT fk_circuitid FOREIGN KEY (circuitid) REFERENCES circuits(circuitid); ok
    ALTER TABLE results ADD CONSTRAINT fk_raceid FOREIGN KEY (raceid) REFERENCES races(raceid);
    ALTER TABLE results ADD CONSTRAINT fk_driverid FOREIGN KEY (driverid) REFERENCES drivers(driverid);ok
    ALTER TABLE results ADD CONSTRAINT fk_constructorid FOREIGN KEY (constructorid) REFERENCES constructors(constructorid);ok
    ALTER TABLE constructorResults ADD CONSTRAINT fk_raceid FOREIGN KEY (raceid) REFERENCES races(raceid);
    ALTER TABLE constructorResults ADD CONSTRAINT fk_constructorid FOREIGN KEY (constructorid) REFERENCES constructors(constructorid);
