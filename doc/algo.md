# Outline
### Components:
```
Data fetching:
    - Data from Docker via public API
````
````
Algorithm:
    In: List car locations + list person location
    Out: Provide API fo webapp
    Components:
        - Mapping cars to persons and estimate Pickup and Arrival times
        - Remember past locations for people and create heatmap for car distribution
        - Manage statistics 
````
````
API:
    - API for webapp
````

## Iterations:
````
Basic
    - use linear sum assignement to get a optimal mapping between cars and customers initially
    - serve all customers and save state
    - loop over api to discover free cars
````


