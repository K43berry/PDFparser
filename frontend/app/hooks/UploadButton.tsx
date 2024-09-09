'use client'

import { useRef } from 'react'
import { Button } from "@/components/ui/button"

const UploadButton = () => {
    const fileInputRef = useRef<HTMLInputElement | null>(null);
  
    const handleButtonClick = () => {
      if (fileInputRef.current) {
        fileInputRef.current.click();
      }
    };
  
    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      const file = event.target.files?.[0];
      if (file) {
        console.log('Selected file:', file);
      }
    };
  
    return (
      <div>
          <Button onClick={handleButtonClick}>Here</Button>
        <input
          type="file"
          ref={fileInputRef}
          style={{ display: 'none' }}
          onChange={handleFileChange}
        />
      </div>
    );
  }
  

export default UploadButton