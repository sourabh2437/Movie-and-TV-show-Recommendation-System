import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.websocket.server.WebSocketHandler;
import org.eclipse.jetty.websocket.servlet.WebSocketServletFactory;


public class Websocket {
	public static void main(String[] args) throws Exception {
   	 // To connect to mongodb server
     //  MongoClient mongoClient = new MongoClient( "localhost" , 27017 );
       // Now connect to your databases
//       DB db = mongoClient.getDB( "test" );
//		 System.out.println("Connect to database successfully");
       Server server = new Server(8080);
       WebSocketHandler wsHandler = new WebSocketHandler() {
           @Override
           public void configure(WebSocketServletFactory factory) {
          factory.register(CopyOfWebsocket1.class);
        //  factory.register(CopyOfWebsocket2.class);
           }
       };
       server.setHandler(wsHandler);
      server.start();
       server.join();
   }
}
