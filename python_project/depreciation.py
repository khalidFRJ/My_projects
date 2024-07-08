def operation (OV , rate , life_time , property ):
    
    if property == "no value":
        return OV * rate * life_time / 100
    elif property == "bodily":
        return OV * rate * life_time / 1200
    elif  property == "intangible":
        return OV * rate * life_time / 1200
    else:
        print("invalled input ")
  
def main ():
    print("calculates the depreciation of your property")
    OV = int(input("Enter the original value : "))
    rate = float(input("Enter the rate : "))
    life_time = int(input("Enter life_time: "))
    property = str(input("Enter the property ( no value, bodily, intangible) : ")).strip().lower()

    result = operation (OV , rate , life_time , property )
    print(f"depreciayion is {result} DH")

if __name__ == "__main__":
    main()
       
