import xmltodict
from glob import glob


if __name__ == "__main__":
    FILE_PATTERN = "data/Takeout/Fit/Activities/**/*.tcx"

    for file in glob(FILE_PATTERN):
        with open(file) as fd:
            doc = xmltodict.parse(fd.read(), force_list={'Activity', 'Lap', 'Trackpoint'})

        print(file)

        laps = [lap for activity in doc["TrainingCenterDatabase"]["Activities"]["Activity"] for lap in activity["Lap"]]
        trackpoints = [tp for lap in laps for tp in lap["Track"]["Trackpoint"]]

        out_filename = file.replace(".tcx", ".csv")

        with open(out_filename, "w") as out_file:
            out_file.write("time,distance,longitude,latitude\n")

            try:
                for trackpoint in trackpoints:
                    time = trackpoint.get("Time")
                    distance = trackpoint.get("DistanceMeters")
                    position = trackpoint.get("Position")
                    lat = lon = ""
                    if position:
                        lat = position["LatitudeDegrees"]
                        lon = position["LongitudeDegrees"]

                    out_file.write("{0},{1},{2},{3}\n".format(time, distance, lon, lat))
            except Exception as e:
                print("Error in file: {0}".format(file))


