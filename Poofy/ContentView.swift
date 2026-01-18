import SwiftUI
import CoreLocation

struct ContentView: View {
    @State private var currentCoordinates: CLLocationCoordinate2D?
    @State private var lastGeneratedFile: String = ""
    
    var body: some View {
        VStack(spacing: 20) {
            Text("Random Location Generator")
                .font(.title)
            
            Text(String(format: "Center: %.5f°N, %.5f°E", Configuration.centerLatitude, Configuration.centerLongitude))
            Text(String(format: "Radius: %.0fm", Configuration.radiusInMeters))
            
            if let coordinates = currentCoordinates {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Generated Location:")
                        .font(.headline)
                    Text(String(format: "Latitude: %.5f°N", coordinates.latitude))
                    Text(String(format: "Longitude: %.5f°E", coordinates.longitude))
                }
                .padding()
                .background(Color.gray.opacity(0.1))
                .cornerRadius(10)
            }
        }
        .padding()
        .onAppear {
            let initialLocation = RandomLocationGenerator.generateRandomLocation()
            currentCoordinates = initialLocation
            lastGeneratedFile = RandomLocationGenerator.updateGPXFile()
        }
        Button("Generate New Location") {
            let newLocation = RandomLocationGenerator.generateRandomLocation()
            currentCoordinates = newLocation
            lastGeneratedFile = RandomLocationGenerator.updateGPXFile()
        
        }
        Button("Cleanup Old GPX Files") {
            RandomLocationGenerator.cleanupOldGPXFiles()
        }
        .buttonStyle(.bordered)
    }
}
#Preview {
    ContentView()

}
