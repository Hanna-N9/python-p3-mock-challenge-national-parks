class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
    
    #Object Relationship Methods and Properties             
    #Returns a list of all trips at a particular national park, Trips must be of type Trip    
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    #Object Relationship Methods and Properties
    #Returns a unique list of all visitors a particular national park has welcomed, Visitors must be of type Visitor
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    #Aggregate and Association Methods
    #Receives a NationalPark object as argument, Returns the total number of times a park has been visited, Returns 0 if the park has no visits
    def total_visits(self):
        return len(self.trips())
    
    #Aggregate and Association Methods
    #Returns the Visitor instance that has visited that park the most, Returns None if the park has no visitors
    def best_visitor(self):   
        visitors = [trip.visitor for trip in self.trips()] 
        return max(set(visitors), key=visitors.count)






class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
            
    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
    
    #Object Relationship Methods and Properties
    #Returns the Visitor object for that trip, Must be of type Visitor        
    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor

    #Object Relationship Methods and Properties
    #Returns the NationalPark object for that trip, Must be of type NationalPark
    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park







class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)
           
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
    
    #Object Relationship Methods and Properties
    #Returns a list of all trips for that visitor, Trips must be of type Trip       
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    #Object Relationship Methods and Properties
    #Returns a unique list of all parks that visitor has visited, Parks must be of type NationalPark
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    #Aggregate and Association Methods
    #Returns the total number of times a visitor visited the park passed in as argument, Returns 0 if the visitor has never visited the park
    def total_visits_at_park(self, park):
        if park.visitors():
            return len([trip for trip in self.trips() if trip.national_park == park])
        return 0 
    
             
    