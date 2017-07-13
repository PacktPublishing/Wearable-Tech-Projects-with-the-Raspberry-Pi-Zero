import gps
import simplekml

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
kml = simplekml.Kml()

i = 0

try:
    while True:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                gpsLon = report.lon
                if hasattr(report, 'lat'):
                    gpsLat = report.lat
                    if hasattr(report, 'alt'):
                        gpsAlt = report.alt
                        gpsName = "Test GPS Point {0}".format(i)
                        print gpsName
                        kml.newpoint(name=gpsName, coords=[(gpsLon,gpsLat,gpsAlt)])
        i = i + 1

except KeyboardInterrupt:
    kml.save("gpsKMLTest.kml")
    quit()
