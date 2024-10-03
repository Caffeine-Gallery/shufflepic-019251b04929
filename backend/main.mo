import Func "mo:base/Func";
import Random "mo:base/Random";
import Text "mo:base/Text";

import Array "mo:base/Array";
import Time "mo:base/Time";
import Nat "mo:base/Nat";

actor {
  // Stable variable to store image URLs
  stable var imageUrls : [Text] = [
    "https://picsum.photos/1920/1080?random=1",
    "https://picsum.photos/1920/1080?random=2",
    "https://picsum.photos/1920/1080?random=3",
    "https://picsum.photos/1920/1080?random=4",
    "https://picsum.photos/1920/1080?random=5"
  ];

  // Function to get a random image URL
  public func getRandomImageUrl() : async Text {
    let seed = Time.now();
    let randomNumber = Nat.abs(seed) % imageUrls.size();
    imageUrls[randomNumber]
  };

  // Function to add a new image URL
  public func addImageUrl(url : Text) : async () {
    imageUrls := Array.append(imageUrls, [url]);
  };

  // Function to get all image URLs
  public query func getAllImageUrls() : async [Text] {
    imageUrls
  };
}
