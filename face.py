class Face:

    def __init__(self, x, y, w, h):
        self.XCoord = x
        self.YCoord = y
        self.Width = w
        self.Height = h
        self.Chair = None

    def connectFacesAndChairs(auditorium, faces): 
        #if they are the same length, every chair has a face, so you would have to choose someone who is paying attention
        if len(auditorium) == len(faces):
            return faces
        for (Face) in faces:
            possibleConnection = [];
            for (Chair) in auditorium:
                if not Chair.Face:
                    #100 is just under the average distance between XCoords of the chairs, so this narrows our search down to the right column
                    if abs(Chair.TopLeft[0] - Face.XCoord) < 100:
                        #the Chair has to be underneath the face, but we want the first one found underneath them
                        if Chair.TopLeft[1] > Face.YCoord:
                            possibleConnection.append([Chair, Chair.TopLeft[1]])
            Face.Chair = possibleConnection[0][0]
            #i think we'll eventually have to save the face to the chair, but at this point chair has changed, so we'd have to add it above
            # Chair.Face = Face
        pass