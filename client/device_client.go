package main

import (
   "strconv"
   "io/ioutil"
   "log"
   "net/http"
   "os"
)

func main() {
   if len(os.Args) > 2 {                       //one client per device
      log.Fatalln("Only provide one device id at a time!")
   }

   if len(os.Args) == 1 {                      //user should provide at least one device
      log.Fatalln("Must provide a device id!")
   }

   device_id := os.Args[1]
   _, err_device_id := strconv.Atoi(device_id)

   if (err_device_id != nil) {
      log.Fatalln("Device id must be an integer!")
   }

   //get device role
   resp, err := http.Get("http://localhost:5000/api/device/" + device_id)
   if err != nil {
      log.Fatalln(err)
   }

   //read body
   body, err := ioutil.ReadAll(resp.Body)
   if err != nil {
      log.Fatalln(err)
   }

   sb := string(body)
   log.Printf(sb)      
}
