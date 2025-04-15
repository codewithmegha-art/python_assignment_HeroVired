import psutil 
import logging 

CPU_USED_THERESHOLD = 80 
MONITORING_INTERVAL = 5 

logging.basicConfig(
    level=logging.INFO , 
     format='%(asctime)s - %(levelname)s - %(message)s'
)  

def monitor_cpu(threshold, interval):

    try :  
        while True :
            current_cpu_usage = psutil.cpu_percent(interval=interval)
            
            if current_cpu_usage > threshold : 
                logging.warning(f"Alert! CPU usage exceeds threshold : {current_cpu_usage}%")
            else : 
                logging.info(f"CPU useage is normal : {current_cpu_usage}%")
        
    except KeyboardInterrupt:
        logging.info("CPU monitoring stopped by user")
        return 
    
    except Exception as e : 
        logging.error(f"An error occurred : {e}")



if __name__ == "__main__":
    monitor_cpu(CPU_USED_THERESHOLD , MONITORING_INTERVAL)