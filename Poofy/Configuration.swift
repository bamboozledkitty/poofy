//
//  Configuration.swift
//  Poofy
//
//  USER GUIDE:
//  Update the values below to change where the app generates locations.
//

import CoreLocation

struct Configuration {
    // MARK: - User Settings
    
    /// The Latitude of the center point (e.g., 12.92156)
    static let centerLatitude: Double = 18.9304041
    
    /// The Longitude of the center point (e.g., 77.66414)
    static let centerLongitude: Double = 72.8272465
    
    /// The radius in meters to generate points within (default: 50)
    static let radiusInMeters: Double = 50
}
