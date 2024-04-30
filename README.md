
# Environmental Health Monitoring System 🌍🔬

## About The Project 📖

The Environmental Health Monitoring System is a real-time application designed to integrate disparate environmental data streams into a unified health metric dashboard. This system utilizes data from CO, NO2, O3, PM2.5, PM10, and SO2 levels, providing immediate monitoring and data-driven decision-making capabilities for personalized respiratory and cardiovascular health during outdoor activities. 🏃‍♂️💨

 - Architected a real-time Environmental Health Monitoring system by integrating disparate environmental data streams, including CO, NO2,
 O3, PM2.5, PM10, and SO2 levels, into a unified health metric dashboard powered by Open Street Maps API. This innovative solution enables
 immediate monitoring and data-driven decision-making for personalized respiratory and cardiovascular health during outdoor exercise events.
- Optimized data collection using cutting-edge API technology, such as the Strava Data API, reducing data inconsistencies by 27% and improving
 accuracy by 35%. Integrated heart rate data for precise breathing volume estimation, mapped with local air quality sensors via constant GPS
 tracking.
- Developed a novel cigarette intake equivalent metric by analyzing air pollution data and individual breathing rates, contributing to improved
 public health research.The methodology and results are documented in a research paper available on [arXiv](https://arxiv.org/abs/1907.10594)


### Built With 🛠️

- [Flask](https://flask.palletsprojects.com/)
- [ArcGIS](https://www.arcgis.com/index.html)
- [Open Street Maps API](https://www.openstreetmap.org/)
- [Strava Data API](https://developers.strava.com/)

## Getting Started 🚀

To get a local copy up and running follow these simple steps.

### Prerequisites 📋

- Python 3.6 or higher
- pip

### Installation 🔧

1. Clone the repo
   ```sh
   git clone https://github.com/yourusername/environmental-health-monitoring.git
   ```
2. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```

## Usage 📊

Run the server:
```sh
python app.py
```
Navigate to `http://localhost:5000/display/<latitude>,<longitude>,<time>,<param>` to view the application.

## Roadmap 🗺️

- [x] Integrate environmental sensors data
- [x] Develop health metric dashboard
- [ ] Add more sensor integrations
- [ ] Implement machine learning for predictive analytics

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📝

Distributed under the MIT License. See `LICENSE` for more information.


