import CoreLocation

struct Location {
    let coordinate: CLLocationCoordinate2D
    
    static let center = CLLocationCoordinate2D(
        latitude: Configuration.centerLatitude,
        longitude: Configuration.centerLongitude
    )
    static let radiusInMeters: Double = Configuration.radiusInMeters
}
