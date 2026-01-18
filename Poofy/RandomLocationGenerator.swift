import CoreLocation
import Foundation

class RandomLocationGenerator {
    static func generateRandomLocation() -> CLLocationCoordinate2D {
        let radiusInDegrees = Location.radiusInMeters / 111000
        
        let u = Double.random(in: 0...1)
        let v = Double.random(in: 0...1)
        let w = radiusInDegrees * sqrt(u)
        let t = 2 * .pi * v
        let x = w * cos(t)
        let y = w * sin(t)
        
        let newLatitude = Location.center.latitude + y
        let newLongitude = Location.center.longitude + x
        
        return CLLocationCoordinate2D(latitude: newLatitude, longitude: newLongitude)
    }
    
    static func updateGPXFile() -> String {
        let randomCoord = generateRandomLocation()
        let timestamp = Int(Date().timeIntervalSince1970)
        let fileName = "RandomLocation_\(timestamp).gpx"
        
        let gpxContent = """
        <?xml version="1.0"?>
        <gpx version="1.1" creator="Poofy">
            <wpt lat="\(randomCoord.latitude)" lon="\(randomCoord.longitude)">
                <name>Random Location within 100m</name>
                <time>\(ISO8601DateFormatter().string(from: Date()))</time>
            </wpt>
        </gpx>
        """
        
        // Save to Documents directory
        if let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            let gpxURL = documentsPath.appendingPathComponent(fileName)
            
            do {
                try gpxContent.write(to: gpxURL, atomically: true, encoding: .utf8)
                print("GPX file created at: \(gpxURL.path)")
                print("Generated Coordinates:")
                print("Latitude: \(randomCoord.latitude)")
                print("Longitude: \(randomCoord.longitude)")
                return fileName
            } catch {
                print("Error creating GPX file: \(error.localizedDescription)")
            }
        }
        return ""
    }
    static func cleanupOldGPXFiles() {
        if let documentsPath = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first {
            do {
                let fileURLs = try FileManager.default.contentsOfDirectory(at: documentsPath,
                                                                         includingPropertiesForKeys: nil)
                for fileURL in fileURLs {
                    if fileURL.pathExtension == "gpx" {
                        try FileManager.default.removeItem(at: fileURL)
                        print("Deleted: \(fileURL.lastPathComponent)")
                    }
                }
            } catch {
                print("Error cleaning up GPX files: \(error.localizedDescription)")
            }
        }
    }
}
